print("let's play game")
print("we have four doors here there is a gift in one door you have to guess the right door (you only have two attends!)")
print("1.door_1")
print("2.door_2")
print("3.door_3")
print("4.door_4")
choose=input("write the number of the door: ")
answer="3"
guess=0
if choose!="1" and choose!="2" and choose!="3" and choose!="4":
   print("choose number between 1 and 4")
   
else:
   

   
   
         
       
   while guess<1:
        
        if choose!=answer:
                choose=input("wrong! (you only have one try),write the number:  ")
                guess+=1
        if choose==answer:
                print("you won!")
                print("$"*10)

        
                break
        else:
             print("you lost!")

  


 