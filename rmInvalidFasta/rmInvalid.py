
'''
This program is designed to remove invalid codon of amino acid

Usage: python rmInvalid.py <inputfile>

Written by: Chase Jhong
'''

from Bio import SeqIO
import sys

valid_aa = set("ACDEFGHIKLMNPQRSTVWY")
sequences = []

# 解析FASTA文件，遍歷每個序列
for record in SeqIO.parse(sys.argv[1], "fasta"):

    record.seq = record.seq.upper()
    # 檢查序列中的每個鹼基是否屬於合法的字源
    if all(base in valid_aa for base in record.seq):
        # 如果是，將該序列添加到新的序列列表中
        sequences.append(record)

# 將新的序列列表寫回到FASTA文件中
SeqIO.write(sequences, "output.fasta", "fasta")
