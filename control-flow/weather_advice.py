# This python script suggests clothing recommendations based on the weather prompt from the user!


weather = input('What\'s the weather like today? (sunny/rainy/cold): ') #prompts the user for weather condition

#writing the if statements to control the output

if weather == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif weather == 'rainy':
    print('Don\'t forget your umbrella and a raincoat.')
elif weather == 'cold':
    print('Make sure to wear a warm coat and a scarf.')
else:
    print('Sorry, I don\'t have recommendations for this weather.')
