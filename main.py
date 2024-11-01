# importing all libraries
from tkinter import *
import random
from tkmacosx import Button
from words import WORDS_T


# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("1000x800")

window.title('Typing Speed Test')
window.configure(background= '#B5C18E')

x = 0

# defining the function for the test
def game():
	global x, seconds, timer_running
	seconds = 0
	timer_running = False

	if x == 0:
		window.withdraw()
		x = x+1

	def update_timer():
		global timer_running, seconds
		if timer_running:
			seconds += 1
			minutes = seconds // 60
			seconds_1 = seconds % 60
			hours = minutes//60
			time_str = f"{hours:02}:{minutes:02}:{seconds_1:02}"
			timer_label.config(text=f'Time: {time_str}')
			windows.after(1000, update_timer)  # Update every 1 second

	# defining function for results of test
	def check_result():
		global timer_running, seconds, correct_words, typing_speed
		timer_running = False
		typing_result = Text(windows, width=100, height=8, font=("Times New Roman", 18), fg = 'black', bg = 'white')
		typing_result.insert(1.0, entry.get("1.0",'end-1c'))
		typing_result.grid(column = 0, columnspan = 3, row = 5, pady = 10)

		entry_list = entry.get("1.0",'end-1c').split(' ')
		print(entry.get("1.0",'end-1c'))
		pos_x = 0
		correct_words = 0
		for n in range(0, len(entry_list)):
			if n >= len(words):
				inde_1 = str(1) + '.' + str(pos_x)
				inde_2 = str(1) + '.' + str(pos_x+len(entry_list[n]))
				typing_result.tag_add('wrong', inde_1, inde_2)
			elif entry_list[n] != words[n]:
					for y in range(0, len(entry_list[n])):
						if y >= len(words[n]):
							inde = str(1) + '.' + str(pos_x + y)
							typing_result.tag_add('wrong', inde)
						elif entry_list[n][y] != words[n][y]:
							inde = str(1) + '.' + str(pos_x+y)
							typing_result.tag_add('wrong', inde)
			elif entry_list[n] == words[n]:
				correct_words +=1
			pos_x += len(entry_list[n]) + 1

		typing_result.tag_config('wrong', foreground= 'red')
		typing_speed = round(correct_words/(seconds/60),0)
		correct_words_l.config(text = f'Correct Words: {correct_words}', fg = '#ffffff')
		typing_speed_l.config(text = f'Typing Speed: {typing_speed} wpm', fg = '#ffffff')


	words = random.choices(WORDS_T, k=100)
	words_text = ' '.join(words)

	windows = Tk()
	windows.geometry("1000x800")
	windows.title('Typing Speed Test')
	windows.configure(background='#B5C18E')
	windows.grid_columnconfigure((0, 1, 2), weight=1, uniform= 'a')

	### timer
	timer_label = Label(windows, text="Time: 00:00:00", font=("Helvetica", 20), background= '#B5C18E', fg = '#524C42')
	timer_label.grid(column = 0, row = 0, pady = 10)

	if not timer_running:
		timer_running = True
		update_timer()

	x2 = Label(windows, text=words_text, font="times 18 italic", bg = '#FAF3F0', fg = 'black',width= 100, height=8, anchor= 'nw', wraplength=880, justify="left")
	x2.grid(column = 0, row = 1, columnspan = 3, pady = 10)

	x3 = Label(windows, text="Start typing in the box below", font="Helvetica 20", background= '#B5C18E', fg = '#524C42')
	x3.grid(column=0, row=2, columnspan = 2, pady=10, padx = 60, sticky = 'w')

	entry = Text(windows, wrap=WORD,width=100, height=8,font=("Times New Roman", 18), bg = 'white', fg = 'black')
	entry.grid(column=0, row=3,columnspan = 3, pady=10)

	f = Frame(windows, background= '#B5C18E')
	f.grid(column=0, row=4, columnspan = 3, pady=10, sticky='w', padx=60)

	b2 = Button(f, text='Done',
					bg='#ffffff', fg='#524C42',
					activebackground='#ffffff',
					font=('Ariel', 15, 'normal'),
					width=200, highlightthickness=0, command=check_result, borderless=1,
				)
	b2.pack(side='left')

	b3 = Button(f, text='Try Again',
				bg='#ffffff', fg='#524C42',
				activebackground='#ffffff',
				font=('Ariel', 15, 'normal'),
				width=200, highlightthickness=0, command=game, borderless=1,
			)
	b3.pack(side='left')


	correct_words_l = Label(windows, text=f'Correct Words: ', font=("Helvetica", 20), background= '#B5C18E', foreground= '#524C42')
	correct_words_l.grid(column=1, row=0, pady=10)

	typing_speed_l = Label(windows, text=f'Typing Speed: ', font=("Helvetica", 20), background= '#B5C18E', foreground= '#524C42')
	typing_speed_l.grid(column=2, row=0, pady=10)

	windows.mainloop()


x1 = Label(window, text="Are You Ready for A Typing Speed Test?", font="Ariel 30", bg = '#B5C18E', fg = '#ffffff')
x1.place(relx = 0.5, rely = 0.3, anchor="center")

b1 = Button(window, text="Go", command=game, width=200, font = 'Ariel 20', bg = '#ffffff',
			activebackground='#B5C18E', highlightthickness=0, borderless=1)
b1.place(relx = 0.5, rely = 0.4, anchor="center")

# calling window
window.mainloop()
