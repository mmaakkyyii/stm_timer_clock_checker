import tkinter as tk

class EntrySet():
    def __init__(self,_name,_unit):
        self.__entry=tk.Entry(width=10)
        self.__name=_name
        self.__unit=_unit

    def put(self, _y,val=''):
        name_text=tk.Label(text=self.__name)
        name_text.place(x=10,y=_y)
        unit_text=tk.Label(text=self.__unit)
        unit_text.place(x=180,y=_y)
        self.__entry.insert(tk.END,val)
        self.__entry.place(x=110,y=_y)

    def GetVal(self):
        try:
            val=int(self.__entry.get());
            return val

        except ValueError:
            print('Enter Number')
            return -1

    def SetVal(self, val):
        self.__entry.delete(0,tk.END)
        self.__entry.insert(tk.END,val)


def Calculation():
    period_s=(period_entry.GetVal()+1) / (clock_frequency_entry.GetVal()/(prescaler_entry.GetVal()+1))
    frequency=1/period_s
    
    print('period   ', end ='')
    print(period_s*1000,end='')
    print(' ms')

    print('frequency ', end ='')
    print(frequency,end='')
    print(' Hz')

    frequenct_entry.SetVal(frequency)
    interrupt_period_entry.SetVal(period_s)



root = tk.Tk()

clock_frequency_entry=EntrySet('clock_frequency','Hz')
period_entry=EntrySet('period','')
prescaler_entry=EntrySet('prescaler','')

frequenct_entry=EntrySet('frequency','Hz')
interrupt_period_entry=EntrySet('period','ms')


root.title("STM32 timer clock checker")
root.geometry("300x180")

text=tk.Label(text='クロック設定')
text.place(x=10,y=10)

check_button = tk.Button(root, text="計算", command=Calculation)
check_button.place(x=100,y=140)

clock_frequency_entry.put(40,72000000)
prescaler_entry.put(60,9)
period_entry.put(80,7199)
frequenct_entry.put(100)
interrupt_period_entry.put(120)

root.mainloop()
        
