# a=int(input('enter a number\n'))
# prime=True
# for i in range(2,a):
#     if i%a==0:
#         prime=False
#         break
# if prime:
#     print('this is prime number')
# else:
#     print('this is not prime number')

# content_ratings=['4+', '9+', '12+', '17+']
# numbers=[4433, 987, 1155, 622]
# content_rating_numbers = [list(x) for x in zip(content_ratings, numbers)]
# print(content_rating_numbers)
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
content_ratings["9+"]="over_9"
content_ratings["17+"]="over_17"
print(content_ratings.get('over_9'))
print(content_ratings.get('over_17'))















    

