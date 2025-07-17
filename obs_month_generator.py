#######################################################################
# Name: Jacob Schlosser
# Program: obs_month_generator
# Purpose: To generate a markdown (.md) file formatted to have every
#          day of a given month with various sections for journalling.
#######################################################################

import os
from datetime import datetime
import calendar

#######################################################################
# Section Variables: Change these to change the template
#######################################################################

# MONTH should always be a capitalized full name
MONTH = "July"
YEAR = "2025"

# Repeating tasks to put on each day entry
TASK_LIST = ["Asleep by 10 P.M."]
# Repeating meal times during each day
DIET_LIST = ["Breakfast", "Lunch", "Dinner", "Snacks"]

#######################################################################
# Section Functions: Small functions called in the main generator function
#######################################################################

def entry_title(month, day):
    title = "## " + month + " " + str(day) + "\n"

    return title

def entry_tasks(task_list):
    task_string = "### Tasks \n"

    for task in task_list:
        task_string = task_string + "- [ ] " + task + "\n"
    
    # Add additional line break at the end of the task list section
    task_string += "\n"
    return task_string

def entry_diet(diet_list):
    diet_string = "### Diet\n"

    for meal in diet_list:
        diet_string = diet_string + meal + ": \n"
    
    # Add additional line break at the end of the diet list section
    diet_string += "\n"
    return diet_string

def entry_journal():
    journal_string = "### Journal Entry\n\n"
    return journal_string

def entry_end():
    end_string = "___\n\n"
    return end_string

#######################################################################
# Generator Function: Function that combines the section functions to
#                     create a .md file with the journal template
#######################################################################

def generate_template(month, year, task_list, diet_list):
    # Turn the string version of month into a month number
    month_num = datetime.strptime(month, "%B").month
    # Get the last day of a month from the tuple returned by monthrange()
    last_day = calendar.monthrange(int(year), month_num)[1]
    
    filename = month + " " + year + ".md"

    # If the template has already been generated, delete 
    if os.path.exists(filename):
        print("Overwriting file: " + filename)
        open(filename, "w").close()
    
    file = open(filename, "a")

    entry_string = ""
    
    for day in range(1,last_day):
        entry_string += entry_title(month, day)
        entry_string += entry_tasks(TASK_LIST)
        entry_string += entry_diet(DIET_LIST)
        entry_string += entry_journal()
        entry_string += entry_end()
        file.write(entry_string)
        entry_string = ""

    file.close()

    print("Finished Program")

generate_template(MONTH, YEAR, TASK_LIST, DIET_LIST)
