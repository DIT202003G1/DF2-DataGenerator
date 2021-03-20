from generators import DummyGenerator, QueriesGenerator
from generators.DummyGenerator import generateOPTIPTAppointment,generatePatient,generateStaff

def main():
    a = generateStaff()
    b = generatePatient()
    c = generateOPTIPTAppointment(b,a)

if __name__ == "__main__":
    main()
