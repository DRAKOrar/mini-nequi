class Usuario:
    def __init__(self):
        self.nombre=[]
        self.cedula=[]
        self.numero=[]
        self.clave=[]
    print(  '''  
                SOMOS NEQUI COLOMBIA    
                    ¡¡BIENVENIDO!!
            para comenzar a disfrutar de nequi 
            debes registrarte''')
    def crearUsuario(self):
        self.opcionUsuario = int(input('''
        ------------------------------------------
        POR FAVOR introduce los siguientes datos en su respectivo orden.. 
        1. Mi nombre
        2. Mi cedula
        3. Mi numero telefonico
        4. Mi clave
        5. Ver mi usuario 
        6. terminar registro
        ingresar:   '''))
        while True:
            if self.opcionUsuario==1:
                self.nombreDef()
            elif self.opcionUsuario==2:
                self.cedulaDef()
            elif self.opcionUsuario==3:
                self.telefonoDef()
            elif self.opcionUsuario==4:
                self.claveDef()
            elif self.opcionUsuario==5:
                self.mostrarUsuario()
            elif self.opcionUsuario>=6:
                break
            else:
                print('LO SENTIMOS OPCION NO VALIDA!, INTENTE DE NUEVO.. ')
                self.crearUsuario()

    def nombreDef(self):
        self.nombre.append(input("ingrese su nombre: "))
        self.nnombre=self.nombre
        print(self.nombre)
        print('''continue con su proceso de registro
        por favor introduce tu cedula: ''')
        self.crearUsuario()

    def cedulaDef(self):
        self.cedula.append(int(input("introduce tu numero de cedula: ")))
        self.ccedula=self.cedula
        print(self.nombre)
        print('''continue con su proceso de registro
        por favor introduce tu contacto: ''')
        self.crearUsuario()
        
    def telefonoDef(self):
        self.numero.append(int(input("por favor introduce tu numero de contacto: ")))
        self.nnumero=self.numero
        print(self.nombre)
        print('''continue con su proceso de registro
        por favor introduce tu clave de usuario:''')
        self.crearUsuario()

    def claveDef(self):
        self.clave.append(int(input("introduce una clave para tu usuario: ")))
        self.cclave=self.clave
        self.crearUsuario()
        
    def mostrarUsuario (self):
        print("\tsu nombre de usuario es: ",self.nnombre)
        print("\tsu cedula es: ",self.ccedula)
        print("\tsu telefono de contacto: ",self.nnumero)
        print("\tsu clave de usuario es: ",self.cclave)
        print('=======================================')
        print('GRACIAS POR USAR NUESTROS SERVICIOS!')
        print('=======================================')
        self.crearUsuario()


class login(Usuario):
    def inter(self):
        print('''
                BIENVENIDO
                ''')
        self.xxnombre=self.nombre.index(str(input("ingrese su usuario: ")))
        self.xnombre=self.nombre[self.xxnombre]    
        print (self.xnombre)
        

        self.xxclave=self.clave.index(int(input("ingrese su contraseña")))
        self.xxclave=self.clave[self.xxclave]    
        print (self.xnombre)
        if self.xxclave==self.xxclave:
            print('''
                BIENVENIDO
                
                ya puedes disfrutar de nequi colombia''')
        else:
            print("intente de nuevo")
            self.inter()
class Cajero(login):
    monto=0
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------------------------
        POR FAVOR INDIQUE QUE OPERACION DESEA REALIZAR.. 
        1. VER SALDO
        2. DEPOSITO A CUENTA
        3. RETIRO DE EFECTIVO
        4. SALIR
        5. MOSTRAR_USUARIO
        ingresar:   '''))
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.saldo()
            elif self.opcion==2:
                self.depositar()
            elif self.opcion==3:
                self.retirar()
            elif self.opcion==4:
                self.control=1
                self.salir()
            else:
                print('LO SENTIMOS OPCION NO VALIDA!, INTENTE DE NUEVO.. ')
                self.operaciones()

    def saldo(self):
        print('SU saldo DISPONIBLE ES: ', self.monto)
        print('DESEA REALIZAR OTRA OPERACION?')
        self.operaciones()

    def depositar(self):
        self.deposito = int(input('INDIQUE LA CANTIDAD A DEPOSITAR.. '))
        self.monto=self.monto + self.deposito
        self.saldo()

    def retirar(self):
        self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
        self.control = 0
        while self.control==0:
            if self.retiro > self.monto:
                print('''NO HAY FONDOS SUFICIENTES!!!..
                --------------------------------------------''')
                self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
            elif self.retiro<= self.monto:
                self.monto=self.monto-self.retiro
                self.control=1
                print('CANTIDAD RETIRADA: ', self.retiro)
                self.saldo()
                

    def salir(self):
        print('=======================================')
        print('GRACIAS POR USAR NUESTROS SERVICIOS!')
        print('=======================================')


ejecucion = Cajero()
ejecucion.crearUsuario()
ejecucion.inter()
ejecucion.operaciones()
