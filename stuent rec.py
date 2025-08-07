import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course

    def __str__(self):
        return f"{self.roll} - {self.name} ({self.course})"


class StudentManager:
    def __init__(self):
        self.students =[]     

    def add_student(self,student):
        self.students.append(student)

    def delete_student(self, roll):
        for s in self.students:
            if s.roll==roll:
                self.students.remove(s)
                return True
        return False   
    def get_all_students(self):
        return [str(s) for s in self.students] 


class StudentApp:
    def __init__(self, root):
        self.manager = StudentManager()
        self.root = root
        self.root.title("Studentn Record Management System")

        tk.Label(root,text="Name").grid(row=0,column=0)
        tk.Label(root,text="Roll No").grid(row=1,column =0)
        tk.Label(root,text="Course").grid(row=2,column=0)
        self.name_entry = tk.Entry(root)
        self.roll_entry = tk.Entry(root)
        self.course_entry = tk.Entry(root)

        self.name_entry.grid(row=0,column=1)
        self.roll_entry.grid(row=1,column=1)
        self.course_entry.grid(row=2,column=1)      

        tk.Button(root,text="Add student",command=self.add_students).grid(row=3,column=0,pady=10)
        tk.Button(root,text="show all ",command=self.show_students).grid(row=3,column=1)
        tk.Button(root,text="delete by roll",command=self.delete_student).grid(row=4,column=0,columnspan=2)


        self.output=tk.Text(root, height=10,width=40)
        self.output.grid(row=5,column=0,columnspan=2,pady=10)

    def add_students(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()
        course = self.course_entry.get()

        if not name or not roll or not course:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        student = Student(name, roll, course)
        self.manager.add_student(student)
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        self.clear_entries()  

    def show_students(self):
        
        students = self.manager.get_all_students()
        if not students:
            messagebox.showinfo("No Students", "No students found!")
            return

        self.output.delete(1.0, tk.END)
        for student in students:
            self.output.insert(tk.END, student + "\n")    


    def delete_student(self):
        roll = self.roll_entry.get()
        if not roll:
            messagebox.showerror("Input Error", "Roll number is required!")
            return

        if self.manager.delete_student(roll):
            messagebox.showinfo("Success", f"Student with roll {roll} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No student found with roll {roll}!")            


    def clear_entries(Self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()      



