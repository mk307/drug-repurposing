from Bio import Align
from Bio import SeqIO
aligner = Align.PairwiseAligner()
aligner.mode = 'local'
aligner.match_score = 1.0
aligner.mismatch_score = -2.0
aligner.gap_score = -2.5
seq1 = SeqIO.read("CRBN.fasta", "fasta")
seq2 = SeqIO.read("IL6.fasta", "fasta")
score = aligner.score(seq1.seq, seq2.seq)
print(score)