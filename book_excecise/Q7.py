'''Write a program to calculate variance and standard deviation of N numbers
                 N    _
    Variance=1/N.∑(xi-x)^2
                 i-1
'''

# Here N is  total number of datapoints
N=list(map(int,input("Enter yor data_points: ").split()))

sum=0
count=0
s_sum=0

# Function to calculate mean by formula = total sum of all numbers/total numbers
for i in N:
    count+=1   # calculating total no. in data_points i.e N
    sum+=i     # calculating total sum of N numbers
X_=sum/count   #here X_ is mean of N numbers
print(f'Mean of {N} is {sum}/{count} = {X_}')
      
for i in N:
    x=(i-X_)**2   #calculating (xi-X_)^2
    s_sum+=x      # And summing them up
    
    print(f'For {i}--> {i}-{X_} = {x}')
    
    Var=s_sum/count    # Calculating variance =(xi-X_)^2/N, here X_ is mean of N numbers
print(f'Sum of squared difference = {s_sum}')    
print(f'Variance = {Var}')
