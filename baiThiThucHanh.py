import mysql.connector

class Patient():
    def __init__(self, **kwargs):
        self.full_name = kwargs.get('full_name', '') 
        self.date_of_birth = kwargs.get('date_of_birth', '1990')   
        self.gender = kwargs.get('gender', '') 
        self.address = kwargs.get('address', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.email = kwargs.get('email', '')
    @classmethod
    def get_cursor(cls):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='py'
        )
        return connection.cursor(), connection

    def get_fields(self):
        
        return {name: value for name, value in self.__dict__.items() if not name.startswith("_")}

    @classmethod
    def get_table_name(cls):
        return "patients"

    def insert(self):
        cursor, connection = self.get_cursor()
        table_name = self.get_table_name()
        fields = self.get_fields()
        columns = ", ".join(fields.keys())
        placeholders = ", ".join(["%s"] * len(fields))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor.execute(sql, list(fields.values()))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        
        return cursor.lastrowid

    @classmethod
    def findAll(cls):
        cursor, connection = cls.get_cursor()
        table_name = cls.get_table_name()
        sql = f"SELECT * FROM {table_name}"
        
        cursor.execute(sql)
        results = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return results if results else None
class Doctor():
    def __init__(self, **kwargs):
        self.full_name = kwargs.get('full_name', '') 
        self.date_of_birth = kwargs.get('date_of_birth', '1990')   
        self.gender = kwargs.get('gender', '') 
        self.address = kwargs.get('address', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.email = kwargs.get('email', '')
    @classmethod
    def get_cursor(cls):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='medical_service'
        )
        return connection.cursor(), connection

    def get_fields(self):
        
        return {name: value for name, value in self.__dict__.items() if not name.startswith("_")}

    @classmethod
    def get_table_name(cls):
        return "doctors"

    def insert(self):
        cursor, connection = self.get_cursor()
        table_name = self.get_table_name()
        fields = self.get_fields()
        columns = ", ".join(fields.keys())
        placeholders = ", ".join(["%s"] * len(fields))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor.execute(sql, list(fields.values()))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        
        return cursor.lastrowid

    @classmethod
    def findAll(cls):
        cursor, connection = cls.get_cursor()
        table_name = cls.get_table_name()
        sql = f"SELECT * FROM {table_name}"
        
        cursor.execute(sql)
        results = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return results if results else None
class Appointment():
    def __init__(self, **kwargs):
        self.patient_id  = kwargs.get('doctor_id ', '') 
        self.doctor_id  = kwargs.get('doctor_id ', '')   
        self.appointment_date  = kwargs.get('appointment_date ', '') 
        self.reason  = kwargs.get('reason', '')
        self.status  = kwargs.get('status', 'Pending')

    @classmethod
    def get_cursor(cls):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='medical_service'
        )
        return connection.cursor(), connection

    def get_fields(self):
        
        return {name: value for name, value in self.__dict__.items() if not name.startswith("_")}

    @classmethod
    def get_table_name(cls):
        return "appointments"

    def insert(self):
        cursor, connection = self.get_cursor()
        table_name = self.get_table_name()
        fields = self.get_fields()
        columns = ", ".join(fields.keys())
        placeholders = ", ".join(["%s"] * len(fields))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor.execute(sql, list(fields.values()))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        
        return cursor.lastrowid

    @classmethod
    def findAll(cls):
        cursor, connection = cls.get_cursor()
        table_name = cls.get_table_name()
        sql = f"SELECT * FROM {table_name}"
        
        cursor.execute(sql)
        results = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return results if results else None

def add_patient():
    name = input("Enter patient name: ")
    date_of_birth = input("Enter patient date of birth: ")
    gender = input("Enter patient gender: ")
    address = input("Enter patient address: ")
    phone_number = input("Enter patient phone number: ")
    email = input("Enter patient email: ")    
    patient = Patient(full_name=name, date_of_birth = date_of_birth,gender = gender,address = address,phone_number=phone_number,email = email)
    patient.insert()
    print("Thêm bệnh nhân thành công")

def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    phone_number = input("Enter doctor phone number: ")
    email = input("Enter doctor email: ")
    year_of_experience = int(input("Enter doctor year of experience: "))
    doctor = Doctor(name, specialization, phone_number, email, year_of_experience)
    doctor.insert()
    print("Thêm bác sĩ thành công")

def add_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    appointment_date = input("Enter appointment date: ")
    reason = input("Enter reason: ")
    status = input("Enter status: ")
    appointment = Appointment(patient_id, doctor_id,appointment_date, reason, status)
    appointment.insert()
    print("Thêm lich hẹn thành công")
                           


if __name__ == "__main__":
    while True:
        print("1. Thêm bệnh nhân")
        print("2. Thêm bác sĩ")
        print("3. Thêm lịch hẹn ")
        print("4. Xem danh sách bệnh nhân")
        print("5. Thoát")
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
            for i in range(3):
                add_patient()
        elif choice == 2:
            for i in range(5):
                add_doctor()
        elif choice == 3:
            add_appointment()
        elif choice == 4:
            print("Danh sách bệnh nhân:")

        elif choice == 5:
            break