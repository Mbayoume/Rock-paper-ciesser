# # import random
# #
# # user_wins = 0
# # computer_wins = 0
# #
# # choice = ['rock', 'paper', 'scissor']
# #
# #
# #
# # # the loop block
# #
# # while True:
# #     user_input = input('type (Rock \ paper \ scissor or Q for quit the game.')
# #
# #     if user_input == 'q'.lower():
# #         print('goodbye')
# #         break
# #
# #         # we use the break method to make the loop stop not to break the programme
# #
# #     if user_input not in choice:
# #         print('please type something valid')
# #         continue
# #     random_number = random.randint(0,2)
# #
# #
# #     computer_pick = choice[random_number]
# #
# #     print('computer picked ',computer_pick)
# #
# #     if user_input == 'rock' and computer_pick == 'scissor':
# #         print('you won')
# #         user_wins +=1
# #
# #
# #     elif user_input == 'scissor' and computer_pick == 'paper':
# #         print('you won')
# #         user_wins +=1
# #
# #     elif user_input == 'paper' and computer_pick == 'rock':
# #         print('you won')
# #         user_wins += 1
# #     elif user_input == computer_pick:
# #         print('draw..  try again')
# #
# #     else:
# #         print('oops you lost')
# #         computer_wins += 1
# #
# # print('you won ' , user_wins ,' times')
# # print('the computer wins ', computer_wins , 'times')
# #
# #
# # ############## creat your own story proeject###############
#
# def start():
#     print('there is a distract in your way ')
#     left_right =  input(' choose your path [left / right ]?\n')
#     if left_right == 'left' or 'LEFT':
#         print(' you have reached to the magic wheel and you need to make a wish')
#     elif left_right == 'right' or 'right'.upper():
#         print(' you have reached to the river ')
#
#
# name = input(' hello; what is your name? \n')
# print('hello',name,'\n')
# des = input(' want to play the game? [yes / No ]\n')
# if des == 'yes'.lower() or 'yes'.upper():
#     print('wooohooo, lets get started.')
#     start()
# elif des == 'no'.lower() or 'no'.upper():
#     print('well this is the end of the journy')
#     quit()
# else:
#     print('hmmmm.... you say what?!')
#

