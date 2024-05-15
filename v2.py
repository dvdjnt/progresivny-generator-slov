from GeneratorViet import GeneratorViet

userinput = input("pocet viet: ")

gen = GeneratorViet()
sen = gen.generateSentences(int(userinput))

print(sen)
