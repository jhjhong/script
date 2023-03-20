--[[
--usage: lua randomsplit.lua seq_fasta 0.7
--arg[1]: input file
--arg[2]: ratio of split
----]]

local function readfq(fp)
	local finished, last = false, nil;
	return function() -- closure
		if finished then return nil end
		if last == nil then -- the first record or a record following a fastq
			for l in fp:lines() do
				if l:byte(1) == 62 or l:byte(1) == 64 then -- ">" || "@"
					last = l;
					break;
				end
			end
			if last == nil then -- reach the end of the file (EOF)
				finished = true;
				return nil;
			end
		end
		local i = last:find("%s"); -- separate the sequence name and the comment
		name, last = i and last:sub(2, i-1) or last:sub(2), nil; -- sequence name
		local seqs, c = {}; -- c is the first character of the last line
		for l in fp:lines() do -- read sequence
			c = l:byte(1);
			if c == 62 or c == 64 or c == 43 then -- ">" || "@" || "+"
				last = l;
				break;
			end
			table.insert(seqs, l); -- similar to python, string cat is inefficient
		end
		if last == nil then finished = true end -- end of file
		if c ~= 43 then return name, table.concat(seqs) end -- a fasta record
		local seq, len = table.concat(seqs), 0; -- prepare to parse quality
		seqs = {};
		for l in fp:lines() do -- read quality
			table.insert(seqs, l);
			len = len + #l;
			if len >= #seq then -- we have read enough qualities
				last = nil;
				return name, seq, table.concat(seqs); -- a fastq record
			end
		end
		finished = true; -- reach EOF
		return name, seq; -- incomplete fastq quality; return a fasta record
	end
end


local function getnseqs(file)
	local nametbl = {}
	local seqtbl = {}
	for name, seq, _ in readfq(file) do
		table.insert(nametbl, name)
		table.insert(seqtbl, seq)
	end
    return nametbl, seqtbl;
end


local function shufflenseqs(nametbl, seqtbl)
	local nametbl_shuffle = {table.unpack(nametbl)}
	local seqtbl_shuffle = {table.unpack(seqtbl)}
	assert(#nametbl == #seqtbl)
	for i = #nametbl_shuffle, 2, -1 do
		local j = math.random(i)
		nametbl_shuffle[i], nametbl_shuffle[j] = nametbl_shuffle[j], nametbl_shuffle[i]
		seqtbl_shuffle[i], seqtbl_shuffle[j] = seqtbl_shuffle[j], seqtbl_shuffle[i]
	end
	return nametbl_shuffle, seqtbl_shuffle
end

local function splitnseqs(nametbl, seqtbl, ratio)
	local ratio = ratio or 0.7 -- defualt ratio: 0.7

	assert(#nametbl == #seqtbl)
	local index = math.floor(#nametbl * ratio)
	local nametbl_train = {table.unpack(nametbl, 1, index)}
	local seqtbl_train = {table.unpack(seqtbl, 1, index)}
	local nametbl_test = {table.unpack(nametbl, index + 1)}
	local seqtbl_test = {table.unpack(seqtbl, index + 1)}
	return nametbl_train, seqtbl_train, nametbl_test, seqtbl_test
end


local function writefasta(nametbl, seqtbl, name)
	assert(#nametbl == #seqtbl)
	local fasta_file = io.open(name, 'w+')
	for i = 1, #nametbl do
		fasta_file:write(">"..nametbl[i].."\n")
		fasta_file:write(seqtbl[i].."\n")
	end
	fasta_file:close()
	return
end

--[[
arg[1]: input file
arg[2]: ratio of split
--]]
math.randomseed(114)
file = io.open(arg[1])

-- Get Sequence table and shuffle it
names, seqs = getnseqs(file)
names, seqs = shufflenseqs(names, seqs)
names_train, seqs_train, names_test, seqs_test = splitnseqs(names, seqs, arg[2])

prefix = string.sub(arg[1], 1, string.len(arg[1]) - 6) -- remove ".fasta"
writefasta(names_train, seqs_train, prefix.."_train.fasta")
writefasta(names_test, seqs_test, prefix.."_test.fasta")
