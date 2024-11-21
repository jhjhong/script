# script
- calengc

簡單統計contigs數量、gc、len等資訊
```console
$ perl calengc.pl <inputfile>
```

- checkm_sum

將CheckM output file (e.g. bin_stats_ext.tsv) 轉為易讀格式
`python3 checkm_summary.py <inputfile> <outputfile>`

- randomseq

隨機將fasta依據比例分組
`lua randomsplit.lua <seq_fasta> ratio`

- rmInvalidFasta

移除fasta不合法字元(amino acid)
`python rmInvalid.py <inputfile>`

