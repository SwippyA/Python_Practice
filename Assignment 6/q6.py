
flower_names = []
print("Please enter the names of 10 flowers:")

for i in range(10):
    flower_name = input(f"Enter flower name {i + 1}: ")
    flower_names.append(flower_name)


print("\nFlower names and their lengths:")
for flower in flower_names:
    print(f"{flower} - Length: {len(flower)}")
