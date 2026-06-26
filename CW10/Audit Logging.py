# --- Estructuras Requeridas --
users = {
    'jperez': {'password': '1234', 'rol': 'student', 'name': 'Juan Pérez'},
    'dromo': {'password': '1234', 'rol': 'student', 'name': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'student', 'name': 'Mauricio Juárez'},
    'mlopez': {'password': '1234', 'rol': 'student', 'name': 'María López'},
    'euc': {'password': '1234', 'rol': 'student', 'name': 'Ernesto Uc'},
    'cbalam': {'password': '1234', 'rol': 'student', 'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics", "Programming", "English II", "Differential Calculus",
    "Probability and Statistics", "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0, 'Differential Calculus': 7.8, 'Probability and Statistics': 8.3, 'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5},
    'dromo': {'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4, 'Differential Calculus': 6.2, 'Probability and Statistics': 9.1, 'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'mjuarez': {'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0, 'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9},
    'mlopez': {'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0, 'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0},
    'euc': {'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0, 'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0},
    'cbalam': {'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 6.6, 'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2}
}


logged_in = False
current_user = ""


while not logged_in:
    u = input("User: ")
    p = input("Password: ")
    if u in users and users[u]['password'] == p:
        current_user = u
        logged_in = True
        print(f"Bienvenid@!, {users[u]['name']} ({users[u]['rol']})")
    else:
        print("Credenciales incorrectas. Intenta de nuevo.")


rol = users[current_user]['rol']

if rol == 'student':
    print("================================")
    print("School Report")
    print("================================")
    aprobadas = set()
    pendientes = set()
    for sub in subjects:
        grade = notes[current_user].get(sub, 0)
        print(f"{sub:35} : {grade}")
        if grade >= 8.0:
            aprobadas.add(sub)
        else:
            pendientes.add(sub)
    print(f"\nApproved: {aprobadas}")
    if len(pendientes) > 0:
        print(f"Pending : {pendientes}")

elif rol == 'professor':
    while True:
        print("================================")
        print("Students")
        print("================================")
        for u, data in users.items():
            if data['rol'] == 'student':
                print(f"User: {u:8} | Student: {data['name']}")
        
        target = input("\nStudent to grade (username): ")
        if target not in notes:
            print("Write other thing to exit")
            break
            
        for sub in subjects:
            print(sub)
            
        materia = input("Subject to grade: ")
        if materia in subjects:
            nueva_nota = float(input("New grade: "))
            print(f"\nDo you confirm (yes/no)?")
            print(f"{materia}: {notes[target][materia]} ==> {nueva_nota}")
            if input().lower() == 'yes':
                notes[target][materia] = nueva_nota
                print("Grade updated!")
                print(notes[target])
        else:
            print("Materia no válida.")

elif rol == 'coordinator':
    print("\n================================")
    print("Records")
    print("================================")
    
    ancho_columna = 8
    header = f"{'SUBJECTS':35}"
    for u in notes:
        header += f"| {u:<{ancho_columna}}"
    print(header)
    
    for sub in subjects:
        fila = f"{sub:35}"
        for u in notes:
            nota = notes[u].get(sub, 0)
            fila += f"| {str(nota):<{ancho_columna}}"
        print(fila)
