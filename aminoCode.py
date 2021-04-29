## Models

class AminoAcid:
  def __init__(self, name, base1, base2):
    self.name = name
    self.base1 = base1
    self.base2 = base2
  
  def __str__(self):
    return self.name

class AminoAcid:
  def __init__(self, name, base1, base2):
    self.name = name
    self.base1 = base1
    self.base2 = base2
  
  def __eq__(self, other):
    return (self.base1 == other) or (self.base2 == other)

## Data informations

transcriptionTable = {"A": "U", "T": "A", "G": "C", "C": "G"}

aminoAcidTable = [ AminoAcid("Alanina"     , "GCU", "GCA"),
                   AminoAcid("Glutamina"   , "CAA", "CAG"),
                   AminoAcid("Arginina"    , "CGG", "CGC"),
                   AminoAcid("Lisina"      , "AAA", "AAG"),
                   AminoAcid("Treonina"    , "ACG", "ACC"),
                   AminoAcid("Leucina"     , "CUU", "UUA"),
                   AminoAcid("Fenilalanina", "UUU", "UUC"),
                   AminoAcid("Aspargina"   , "AAC", "AAU")
                 ]

def transcriptionToRNA(dna):
  rna = ""
  for base in dna:
    rna  += transcriptionTable[base]
  return rna 

def findAminoAcidName(base):
  for aminoAcid in aminoAcidTable:
    if aminoAcid == base:
      return aminoAcid.name
  return ""

def createBaseMatrix(rna):
  baseMatrix = []
  step = 3

  for index in range(len(rna)+1-step):
    base = rna[index:step+index]
    name = findAminoAcidName(base)

    baseMatrix.append((base, name))
  
  return baseMatrix

def createOutput(dna, rna, baseMatrix):
  print("\nDNA: {0}".format(dna))
  print("RNA: {0}\n".format(rna))
  print("Aminoácidos identificados:\n")

  occurrences = {}

  for aminoAcid in baseMatrix:
    if aminoAcid[1] != "":
      print("{0} - {1}".format(aminoAcid[0], aminoAcid[1]))

      try:
        occurrences[aminoAcid[1]] = occurrences[aminoAcid[1]] + 1
      except:
        occurrences[aminoAcid[1]] = 1
  
  print("\nForam identificados {0} aminoácidos diferentes.".format(len(occurrences)))
  
  for name, occurrence in occurrences.items():
    if occurrence > 1:
      print("A {0} foi identificada {1} vezes na sequência.".format(name,occurrence))
    
    
userInput = input("Escreva a sequência de DNA: ")

rna = transcriptionToRNA(userInput)

baseMatrix = createBaseMatrix(rna)
createOutput(userInput, rna, baseMatrix)
