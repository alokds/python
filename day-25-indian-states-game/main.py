import turtle
import pandas as pd

##******************Use turtle  to add INDIA MAP**************************************
screen = turtle.Screen()
screen.title("INDIA STATE GAME")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)

##*********************Read the state file ******************************************
states = pd.read_csv("indian_states.txt")

#********************Convert the state series to LIST *****************************
state_list = states.state.to_list()
state_count= len(state_list)

# ****************** Print state and count Score ***************************************
# missing_list = []
answer_list = []

score = 0
e='Exit'
exit = e.title()
t = turtle.Turtle()
while score < state_count:

    # with open("answer_sheet.txt", mode ='w') as answer_sheet:
    #     answer_sheet.write("")
    state = screen.textinput(title=f"{score}/{state_count} is correct", prompt="Guess anotherstate name")
    state_name = state.title() 
    answer_list.append(state_name) 

     #############   below syntax using list comprehension ################ 
    if state_name == exit:
        missing_list = [s for s in state_list if s not in answer_list]  
        missing = pd.DataFrame(missing_list)
        missing.to_csv("answer_sheet.txt")
        answer = pd.read_csv("answer_sheet.txt")
       
   
                # missing_list.append(s)
        #         with open(f"answer_sheet.txt", mode='a') as missing_states:
        #              missing = missing_states.write(f"{s}\n")
        t.penup()
        t.hideturtle()
        t.goto(x=250, y=-100)
        t.write(f"you missed below states: \n {answer}")
        break
       
    if state_name in state_list:
        # t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_record =  states[states.state == state_name]
        t.goto(state_record.x.item(), state_record.y.item())
        t.write(state_record.state.item())
        score = score +1
    
    


# def get_mouse_click_coords(x, y):
#    print(f"Clicked at: X={x}, Y={y}")

# screen.onclick(get_mouse_click_coords)
# screen.listen()
# screen.mainloop()
        
screen.exitonclick()