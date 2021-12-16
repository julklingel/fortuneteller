from django.shortcuts import render
import random 

# Create your views here.

def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        'fortune': f'You will get {fortune}.'
    }
    return render(request,'randomfortune/fortune.html', context)
    



fortuneList = [
    "a horse", "a banana", "water", "coal", "nothing", "a bucket of chickenwings", "a puppy", "rolex watch"
  
]