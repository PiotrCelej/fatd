#elementy losowe, jakie występują w FATD na podstawie rzutów kośćmi
import random
def roll_dice(num_dice, num_sides):
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

print("Rzut 2k6:", roll_dice(2, 6))
