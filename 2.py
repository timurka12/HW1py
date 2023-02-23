from collections import Counter
import re

text = '''The number of protons in the nucleus (the charge number, also the ordinal number of the element) is usually denoted by Z, the number of neutrons is denoted by N. Their sum A = Z + N is called the kernel mass number. Atoms with the same Z (that is, atoms of the same element), but different N are called isotopes, with the same A, but different Z — isobars, with the same N, but different Z — isotones.

The main difference between a proton and a neutron is that a proton is a charged particle whose charge e = 4.801⋅10-10 units. SGSE = 1.602⋅10-19 Kl. This is an elementary charge, modulo equal to the charge of an electron. The neutron, as its name already shows, is electrically neutral. The spins of the proton and neutron are the same and equal to the spin of the electron, that is 1/2 (in units of {\displaystyle\hbar }\hbar, Planck's constant). The masses of the proton and neutron are almost equal: 1836.15 and 1838.68 electron masses, respectively.
'''

yadro = Counter(i for i in re.findall(r'[A-z\']{2,}', text))
print(yadro.most_common(10))