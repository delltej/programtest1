salary=float(input("please enter your salary in Germany:"))
country=input("enter the country you want to migrate to:")

def convertsalary (country, salary) :
 if (country == "canada"):
    final_salary = salary * 1.55

    if (final_salary > 64000):
            print ("You will be rich in Canada with a salary of ", final_salary, " CAD")
    else:
            print ("You will be poor in Canada with a salary of ", final_salary, " CAD")

 elif  (country == "united kingdom"):
    final_salary = salary * 2.5

    if (final_salary >35000) :
      print("You will be rich in United Kingdon with a salary of ", final_salary, " Pound")
    else:
      print ("You will be poor in united kingdom with a salary of ", final_salary, " Pound")

 elif (country == "cambodia"):
    final_salary = salary * 4555
    if (final_salary >5649856) :
      print ("You will be rich in cambodia with a salary of ", final_salary, "cambodian riel")
    else:
      print ("You will be poor in cambodia with a salary of ", final_salary, "cambodian riel")

 elif (country == "US"):
      final_salary = salary * 1.2
      if (final_salary >56516) :
       print("You wiil be rich in US as with a salary of ", final_salary, "USD")
      else:
       print("You will be poor in US with a salary of ", final_salary, "USD")
 else:
       print("Invalid country")
 
convertsalary(country,salary)