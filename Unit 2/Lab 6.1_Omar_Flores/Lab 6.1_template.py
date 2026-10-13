import tkinter as tk
from tkinter import ttk
import os
from abc import ABC, abstractmethod
from datetime import datetime

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass


class SmarTv(SmartDevice):
    def __init__(self):
        super().__init__("LG Tv")

    def turn_on(self) -> str:
        return f"{self.name} is on channel Azteca 7."

    def turn_off(self) -> str:
        return f"{self.name} is turning off and entering standby mode."


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Echo Dot 5")

    def turn_on(self) -> str:
        return f"{self.name} is playing Lofi music at volume 20%."

    def turn_off(self) -> str:
        return f"{self.name} stopped music playback and muted microphone."


class SmartWatch(SmartDevice):
    def __init__(self):
        super().__init__("Apple Watch")

    def turn_on(self) -> str:
        return f"{self.name} is receiving a call."

    def turn_off(self) -> str:
        return f"{self.name} screen locked and Do Not Disturb enabled."

class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Nest Thermostat")

    def turn_on(self) -> str:
        return f"{self.name} is heating room to 22°C."

    def turn_off(self) -> str:
        return f"{self.name} eco mode activated. Heating paused."


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6: Polymorphism GUI By Omar Gabriel Flores Castro")
        self.geometry("520x560")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "app_icon.png")

        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto(True, self.app_icon)
        else:
            print("The icon file doesn't exist")

        self.items = {
            "Tv": SmarTv(),
            "Speaker": SmartSpeaker(),
            "Watch": SmartWatch(),
            "Thermostat": SmartThermostat(),
        }

        self._build_interface()

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Times New Roman", 26, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=10)

        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=8
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        btn_on = tk.Button(
            btn_frame,
            text="Turn On",
            command=lambda: self._handle_action(action="on"),
            bg="#11c35b",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_on.pack(side="left", padx=10)

        btn_off = tk.Button(
            btn_frame,
            text="Turn Off",
            command=lambda: self._handle_action(action="off"),
            bg="#7a1a10",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            cursor="hand2",
            padx=15,
            pady=5
        )
        btn_off.pack(side="left", padx=10)

        self.lbl_output = tk.Label(
            self,
            text="Select an option above and control your smart device.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=2,
            wraplength=460,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 11, "bold")
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log_list = tk.Listbox(log_frame, height=6, font=("Consolas", 9))
        self.log_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(log_frame, command=self.log_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_list.config(yscrollcommand=scrollbar.set)

    def _handle_action(self, action: str):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]

        if action == "on":
            result_message = active_object.turn_on()
        else:
            result_message = active_object.turn_off()

        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))

        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {result_message}"
        self.log_list.insert(tk.END, log_entry)
        self.log_list.see(tk.END)

if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()