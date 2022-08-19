
def format_name(f_name,l_name):
  return (f_name +' ' +l_name).title()

#print(format_name('vikas','srivastava'))

def is_leap(year):
  if year%4==0:
    if year%100==0:
      if year%400==0:
        return True
      else:
        return False
    else:
      return True
  return False

def days_month(year,month):
  Months=[31,28,31,30,31,30,31,31,30,31,30,31]
  if is_leap(year) and month==2:
    return 29
  return Months[month - 1]

year=int(input("provide year : "))
month=int(input("provide month: "))
days=days_month(year,month)
print(days)