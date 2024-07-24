class Biomolecule:

    def __init__(self, seq_name, seq) -> None:
        self.seq_name = seq_name
        self.seq = seq

    def __str__(self):   
        return '>' + self.seq_name + '\n' + self.seq
    
    valid_characters = ['A', 'B', 'C', 'D']

    def is_valid(self, valid_characters= valid_characters) -> bool:
        return len(set(self.seq) - set(valid_characters)) == 0
            
    def extract_seq(self, start_pos, end_pos):
        if end_pos < start_pos:
            (start_pos, end_pos) = (end_pos,start_pos)
        if start_pos <0:
            start_pos = 0
            print('Start position was can\'t be negative. Start position adjusted to 0.')
        if end_pos> len(self.seq) -1:
            print('End position was greater than sequence length. End position adjusted to the end of the sequence.')
            end_pos = len(self.seq) -1
        return self.seq[start_pos: end_pos]
    

class Carbohydrate(Biomolecule):
    valid_characters = ['P', 'Q', 'R', 'S']
    def is_valid(self, valid_characters=valid_characters) -> bool:
        return super().is_valid(valid_characters)

class Nucleotide(Biomolecule):
    valid_characters = ['W' ,'X','Y','Z']
    def is_valid(self, valid_characters=valid_characters) -> bool:
        return super().is_valid(valid_characters)
    
    def mutate(self, pos, altered_seq, valid_characters = valid_characters):
        if altered_seq in valid_characters:
            x =list(self.seq)
            x[pos] = altered_seq
            self.seq = ''.join(x)
        else:
            print(f'Sequence not mutated. {altered_seq} is not a valid character for the sequence type of {self.seq_name}')

class Protein(Nucleotide):
    valid_characters = ['K', 'L', 'M', 'N']
    def is_valid(self, valid_characters=valid_characters) -> bool:
        return super().is_valid(valid_characters)
    def mutate(self, pos, altered_seq, valid_characters=valid_characters):
        return super().mutate(pos, altered_seq, valid_characters)

bioseq = Biomolecule(seq_name='ABC_test', seq='BCDDD')

print(bioseq)

print(bioseq.is_valid())

print(bioseq.extract_seq(3,1))

carb = Carbohydrate(seq_name='carb_q', seq='PQRS')

print(carb)
print(carb.is_valid())

dna = Nucleotide(seq_name='primer', seq='XYZ')

print(dna.is_valid())

print(dna)
dna.mutate(2,'X')
print(dna)

protein = Protein(seq_name='protein_x', seq='KLMN')

print(protein)
protein.mutate(2,'X')
print(protein)
