print("welcome to ISG")
acc = input("do you have an account ")
if acc =="yes":
   

   print("Please Login:\n")
   user_name= input("username: ")
   pass_ = input("password: ")
   
   
   print("welcome to your child's profile, what would you like to see?")  
   print("\n1.Behavious ,\n2.Accademic, \n3.Sports\n4.Homework")
   select = input("select any")
   if select =="1":
      print("Sipho's profile")
      print("\n -Sipho is noisy in class \n -He eats during lessons")
   elif select == "2":
      print("formal task april 30\45")
      print("formal task may 12\20")
      print("formal task june 30\30")
   elif select == "3":
        print("1st place in javeline")
        print("3st place in long jump")
        print("1st place in athletics")
        other_sports="NA"
        
        
        while other_sports ==True:
            print(other_sports)
            break
            

   count = 2
   pass_ = input("enter password")
   while count > 0:

       if pass_=="1234":
        print("welcome")
        break
       else:
          
           retry_= input("retry password")
       if  retry_== pass:
           count -= 1
           print("Login failed")
           break
        
elif acc =="no":
     print("Please Register")
     first_name = input("name: ")
     surname = input("surname: ")
     email = input("email: ")
     pass_word =input("password: ")
     print("confirm password: ")
     pass_word2 = input("confirm password")
     if  pass_word == pass_word2:
         print("account confirmed")
         print("welcome to your child's profile, what would you like to see?")  
         print("\n1.Behavious ,\n2.Accademic, \n3.Sports\n.3Homework")
     else:
         print("PASSWORD doesn't match")
         quit()

        
else:
    quit()
