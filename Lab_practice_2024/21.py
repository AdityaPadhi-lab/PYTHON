import math
height=(float)(input("Enter the height: "))
gravity=9.8
initial_velo=0
final_velo=math.sqrt(initial_velo**2 + 2*gravity*height)
print(f"the final velpocity of the object when it hits the ground is: {final_velo: .2f} m/s")