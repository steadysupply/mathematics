import utils

consumption = utils.r_dataset('mtcars')['mpg']
print(utils.iqr(consumption))
