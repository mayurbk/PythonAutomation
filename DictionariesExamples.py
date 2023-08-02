##to extract a list of values from a given list of dictionaries
def test(lst,marks):
    result = [a[marks] for a in lst if marks in a] #
    return result

marks = [{"Math":90, 'science':89},
         {'Math':78,'science':86},
         {'Math':94,'science':92}]

print("Original Dictionary:")
print(marks)
subj = "science"
print("Extracting the list of values from list of dictionaries where subject = ",subj)
print(test(marks,subj))

print("original dictioanry")
print(marks)
subj = "Math"
print("Extracting the list of values from list of dictionaries where subject = ",subj)
print(test(marks,subj))