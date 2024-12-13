# Second Mini-Program in FreeCodeCamp Python Certification

def add_time(start_time, duration, curr_day=None):
    # parse the input
    curr_hr, curr_mn = map(int, start_time.split(' ')[0].split(':'))
    period = start_time.split(' ')[1]
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if curr_day:
        curr_day = curr_day.lower()
    hr, mn = map(int, duration.split(':'))
    day_cnt = 0 # to compute the days passed
    
    # adjust hour change if minutes > 60
    final_mn = (curr_mn + mn) % 60
    if curr_mn + mn >= 60:
        hr += 1
    
    # compute final hr and number of flips for am/pm
    prd_flip = hr // 12
    hr_change = hr % 12

    final_hr = hr_change+curr_hr
    
    if final_hr > 12:
        final_hr -= 12
        prd_flip += 1
    elif final_hr == 12:
        prd_flip += 1
    
    # compute days passed
    if period == 'PM':
        # days will pass only for PM to AM change
        day_cnt = prd_flip//2 + prd_flip%2
    else:
        day_cnt = prd_flip//2
    
    # days passed string based on day is provided or not
    final_day = None
    if curr_day:
        idx = days.index(curr_day)
        final_idx = (idx + day_cnt) % 7
        final_day = days[final_idx].capitalize()
        
    
    # adjust am pm, if flip is even then no change as it will remain same after every 2 flips
    if prd_flip % 2 != 0:
        period = 'AM' if period == 'PM' else 'PM'
    
    final_mn = str(final_mn).rjust(2, '0')
    new_time = f'{final_hr}:{final_mn} {period}'
    
    if curr_day:
        new_time += f', {final_day}'
    if day_cnt == 1:
        new_time += ' (next day)'
    elif day_cnt > 1:
        new_time += f' ({day_cnt} days later)'
    
    return new_time
    

# add_time('3:00 PM', '3:10')
# # Returns: 6:10 PM
# print("=======================")

# add_time('11:30 AM', '2:32', 'Monday')
# # Returns: 2:02 PM, Monday
# print("=======================")

# add_time('11:43 AM', '00:20')
# # Returns: 12:03 PM
# print("=======================")

# add_time('10:10 PM', '3:30')
# # Returns: 1:40 AM (next day)
# print("=======================")

# add_time('6:30 PM', '205:12')
# # Returns: 7:42 AM (9 days later)
# print("=======================")

# add_time('11:43 PM', '24:20', 'tueSday')
# # Returns: 12:03 AM, Thursday (2 days later)
# print("=======================")