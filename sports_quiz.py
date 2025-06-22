import time
print('WELCOME TO MY GAME')
print()
print('CHOOSE A CLUB TO QUIZ TO TEST YOUR KNOWLEDGE')
print('1. Barcelona')
print('2. Real Madrdid')
print('3. Bayern Munich')
print('4. Liverpool')
print('5. Exit')

a = int(input('Enter your choice (1/2/3/4/5): '))

if a == 1:
    time.sleep(1)
    print()
    print('YOU HAVE CHOSEN BARCELONA')
    print('ANSWER THE FOLLOWING 10 QUESTIONS')
    print('THE QUIZ BEGINS NOW')
    time.sleep(2)
    print()
    def barca():
        Q = [
            {
                "Question": "Who is the top scorer for Barcelona?",
                "Options": "a) Messi\nb) Pedro\nc) Suarez\nd) Neymar",
                "Answer": "a"
            },
            {
                "Question": "How many Laligas has Barcelona won as of 5/20/2025?",
                "Options": "a) 27\nb) 28\nc) 30\nd) 51",
                "Answer": "b"
            },
            {
                "Question": "What was the most dangerous attack in Barca called?",
                "Options": "a) BBC\nb) MNS\nc) SNM\nd) MSN",
                "Answer": "d"
            },
            {
                "Question": "How many champions leagues has Barca won?",
                "Options": "a) 12\nb) 15\nc) 5\nd) 3",
                "Answer": "c"
            },
            {
                "Question": "How many Ballon d'ors does Barca's players have in history?",
                "Options": "a) 12\nb) 8\nc) 23\nd) 10",
                "Answer": "a"
            },
            {
                "Question": "Who is Barca's Catalunyn derby with?",
                "Options": "a) Real Madrid\nb) Espanyol\nc) Atletico Madrid\nd) Villareal",
                "Answer": "b"
            },
            {
                "Question": "Who is the youngest scorer for Barcelona in its history?",
                "Options": "a) Messi\nb) Dani Alves\nc) Ronaldo\nd) Yamal",
                "Answer": "d"
            },
            {
                "Question": "Who currently wears the no.10 in Barca as of 5/20/2025?",
                "Options": "a) Messi\nb) Fati\nc) Ronaldo\nd) Yamal",
                "Answer": "b"
            },
            {
                "Question": "Who is the most hated Barca player ever?",
                "Options": "a) Messi\nb) Figo\nc) Ronaldo\nd) Pedro",
                "Answer": "b"
            },
            {
                "Question": "When did Barca go bankrupt?",
                "Options": "a) 2021\nb) 2017\nc) 2020\nd) Never",
                "Answer": "a"
            }
        ]

        index = 0
        score = 0
        count = len(Q)

        while index < count:
            q = Q[index]  
            print(f"{index + 1}. {q['Question']}")
            print(q['Options'])

            answer = input("Your answer (a/b/c/d): ")

            if answer.lower() == q['Answer'].lower():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!")

            index += 1

        print(f"Your final score is: {score}/{count}")

    barca()
elif a==2:
    time.sleep(1)
    print()
    print('YOU HAVE CHOSEN REAL MADRID')
    print('ANSWER THE FOLLOWING 10 QUESTIONS')
    print('THE QUIZ BEGINS NOW')
    time.sleep(2)
    print()
    def madrid():
        Q = [
            {
                "Question": "Who is the top scorer for Real Madrid?",
                "Options": "a) Ronaldo\nb) Raul\nc) Stefano\nd) Benzema",
                "Answer": "a"
            },
            {
                "Question": "How many Laligas has Madrid won as of 5/20/2025?",
                "Options": "a) 27\nb) 23\nc) 36\nd) 51",
                "Answer": "c"
            },
            {
                "Question": "What was the attack in Madrid called?",
                "Options": "a) BCB\nb) BBC\nc) CBB\nd) MSN",
                "Answer": "b"
            },
            {
                "Question": "How many champions leagues has Madrid won?",
                "Options": "a) 12\nb) 15\nc) 16\nd) 4",
                "Answer": "b"
            },
            {
                "Question": "How many Ballon d'ors does Madrid's players have in history?",
                "Options": "a) 12\nb) 8\nc) 23\nd) 10",
                "Answer": "a"
            },
            {
                "Question": "Who is Madrid's derby with?",
                "Options": "a) Barcelona\nb) Celta Vigo\nc) Atletico Madrid\nd) Villareal",
                "Answer": "c"
            },
            {
                "Question": "Who is the youngest scorer for Madrid in its history?",
                "Options": "a) Nico\nb) Mbappe\nc) Ronaldo\nd) Endrick",
                "Answer": "d"
            },
            {
                "Question": "Who currently wears the no.7 in Madrid as of 5/20/2025?",
                "Options": "a) Vini\nb) Mbappe\nc) Ronaldo\nd) Bellingham",
                "Answer": "a"
            },
            {
                "Question": "Who is the most expensive signing of madrid?",
                "Options": "a) Mbappe\nb) Hazard\nc) Ronaldo\nd) Bellingham",
                "Answer": "b"
            },
            {
                "Question": "When did Madrid last win a treble?",
                "Options": "a) 2020\nb) 2017\nc) 2009\nd) Never",
                "Answer": "d"
            }
        ]

        index = 0
        score = 0
        count = len(Q)

        while index < count:
            q = Q[index]  
            print(f"{index + 1}. {q['Question']}")
            print(q['Options'])

            answer = input("Your answer (a/b/c/d): ")

            if answer.lower() == q['Answer'].lower():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!")

            index += 1

        print(f"Your final score is: {score}/{count}")

    madrid()
elif a==3:
    time.sleep(1)
    print()
    print('YOU HAVE CHOSEN BAYERN MUNICH')
    print('ANSWER THE FOLLOWING 10 QUESTIONS')
    print('THE QUIZ BEGINS NOW')
    time.sleep(2)
    print()
    def bayern():
        Q = [
            {
                "Question": "Who is the top scorer for Bayern Munich?",
                "Options": "a) Muller\nb) Lewandowski\nc) Ribery\nd) Robben",
                "Answer": "a"
            },
            {
                "Question": "How many Bundesliga has Bayern won as of 5/20/2025?",
                "Options": "a) 27\nb) 28\nc) 33\nd) 51",
                "Answer": "c"
            },
            {
                "Question": "What was the roberry?",
                "Options": "a) Ribery+Robben\nb) Robben+Reus\nc) Ribery+Reus\nd) Muller+Ribbon",
                "Answer": "a"
            },
            {
                "Question": "How many champions leagues has Bayern won?",
                "Options": "a) 12\nb) 7\nc) 4\nd) 6",
                "Answer": "d"
            },
            {
                "Question": "How many Ballon d'ors does Bayern's players have in history?",
                "Options": "a) 12\nb) 5\nc) 2\nd) 10",
                "Answer": "b"
            },
            {
                "Question": "Who is Bayern's derby with?",
                "Options": "a) Nurnberg\nb) Dortmund\nc) Hamburg\nd) Hoffenheim",
                "Answer": "a"
            },
            {
                "Question": "Who is the youngest scorer for Bayern in its history?",
                "Options": "a) Sane\nb) Musiala\nc) Tel\nd) William",
                "Answer": "c"
            },
            {
                "Question": "Who spent 25 years at the club to leave in 2025?",
                "Options": "a) Sane\nb) Muller\nc) Neuer\nd) Kane",
                "Answer": "b"
            },
            {
                "Question": "What is Bayern's highest ever streak in winning the Bundesliga?",
                "Options": "a) 14\nb) 15\nc) 20\nd) 11",
                "Answer": "d"
            },
            {
                "Question": "When Bayern's winning streak come to an end?",
                "Options": "a) 2023\nb) 2022\nc) 2020\nd) 2018",
                "Answer": "a"
            }
        ]

        index = 0
        score = 0
        count = len(Q)

        while index < count:
            q = Q[index]  
            print(f"{index + 1}. {q['Question']}")
            print(q['Options'])

            answer = input("Your answer (a/b/c/d): ")

            if answer.lower() == q['Answer'].lower():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!")

            index += 1

        print(f"Your final score is: {score}/{count}")

    bayern()
elif a==4:
    time.sleep(1)
    print()
    print('YOU HAVE CHOSEN LIVERPOOL')
    print('ANSWER THE FOLLOWING 10 QUESTIONS')
    print('THE QUIZ BEGINS NOW')
    time.sleep(2)
    print()
    def liver():
        Q = [
            {
                "Question": "Who is the top scorer for Liverpool?",
                "Options": "a) Rush\nb) Nunez\nc) Salah\nd) Firmino",
                "Answer": "a"
            },
            {
                "Question": "How many Premier Leagues has Liverpool won as of 5/20/2025?",
                "Options": "a) 17\nb) 28\nc) 20\nd) 19",
                "Answer": "c"
            },
            {
                "Question": "Who is regarded as the Egyptian King?",
                "Options": "a) Salah\nb) Marmoush\nc) Firminio\nd) Mane",
                "Answer": "a"
            },
            {
                "Question": "How many champions leagues has Liverpool won?",
                "Options": "a) 12\nb) 7\nc) 4\nd) 6",
                "Answer": "d"
            },
            {
                "Question": "How many Ballon d'ors does Liverpool's players have in history?",
                "Options": "a) 12\nb) 1\nc) 2\nd) 10",
                "Answer": "b"
            },
            {
                "Question": "Who is Liverpool's derby with?",
                "Options": "a) Tottenham\nb) Arsenal\nc) Everton\nd) Wolves",
                "Answer": "c"
            },
            {
                "Question": "Who is the youngest scorer for Liverpool in its history?",
                "Options": "a) Mane\nb) Ben\nc) Grit\nd) Salah",
                "Answer": "b"
            },
            {
                "Question": "Who did the 'slip'?",
                "Options": "a) Salah\nb) Gerrard\nc) Szoboszlai\nd) Gravenburch",
                "Answer": "b"
            },
            {
                "Question": "What is Liverpool's highest unbeaten streak?",
                "Options": "a) 48\nb) 45\nc) 30\nd) 49",
                "Answer": "d"
            },
            {
                "Question": "When did Klopp win his only Premier league?",
                "Options": "a) 2020\nb) 2021\nc) 2019\nd) 2018",
                "Answer": "a"
            }
        ]

        index = 0
        score = 0
        count = len(Q)

        while index < count:
            q = Q[index]  
            print(f"{index + 1}. {q['Question']}")
            print(q['Options'])

            answer = input("Your answer (a/b/c/d): ")

            if answer.lower() == q['Answer'].lower():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!")

            index += 1

        print(f"Your final score is: {score}/{count}")

    liver()
else:
    print ()
    print ('THANK YOU FOR PLAYING')
    time.sleep(3)
    quit()
