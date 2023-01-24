from flask import Flask, request, jsonify
import mysql.connector as mysql

app = Flask(__name__)

mydb = mysql.connect(
        host="localhost",
        user="py",
        password="example",
        database="materiel",
        port = "3307",
    auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()

# Pour la database "Materiel"

@app.route('/read/<id>', methods=['GET'])
def read(id):
    # Read the data from the MySQL database
    sql = f"""SELECT * FROM Materiel WHERE id = {id}"""
    mycursor.execute(sql)
    user = mycursor.fetchone()

    if user is None:
        return jsonify({'message': 'No user found with the given id'})
    else:
        user_json = [{"id":user[0], "nom_du_produit": user[1], "dimensions":user[2], "etat":user[3]}]

    return jsonify(user_json)

@app.route('/getall', methods=['GET'])
def read():
    # Read the data from the MySQL database
    sql = f"""SELECT * FROM Materiel"""
    mycursor.execute(sql)
    users = mycursor.fetchall()

    users_json = []
    for user in users:
        users_json.append({"id":user[0], "nom_du_produit": user[1], "dimensions":user[2], "etat":user[3]})

    return jsonify(users_json)

@app.route('/update', methods=['PUT'])
def update():
    if request.method == 'PUT':
        data = request.get_json()
        # Read the data from the MySQL database
        sql = f"""UPDATE Materiel SET nom_du_produit = "{data["nom_du_produit"]}", dimensions = "{data["dimensions"]}", etat = "{data["etat"]}" WHERE id = {data["id"]}"""
        
        mycursor.execute(sql)
        mydb.commit()

        return {"result":"Update was made"}

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    # Delete the data from the MySQL database
    sql = f"""DELETE FROM Materiel WHERE id = {id}"""
    mycursor.execute(sql)
    mydb.commit()

    # Return a success message
    return jsonify({'message': 'User deleted successfully'})

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        data = request.get_json()
        # Read the data from the MySQL database
        sql = f"""INSERT INTO Materiel (nom_du_produit, dimensions, etat) VALUES ("{data["nom_du_produit"]}", "{data["dimensions"]}", "{data["etat"]}")"""
        
        mycursor.execute(sql)
        mydb.commit()

# Pour la database "Employe"

@app.route('/read/<id>', methods=['GET'])
def read(id):
    # Read the data from the MySQL database
    sql = f"""SELECT * FROM Employe WHERE id = {id}"""
    mycursor.execute(sql)
    user = mycursor.fetchone()

    if user is None:
        return jsonify({'message': 'No user found with the given id'})
    else:
        user_json = [{"id":user[0], "nom": user[1], "prenom":user[2], "age":user[3], "profession":user[4]}]

    return jsonify(user_json)




if __name__ == '__main__':
    app.run(debug=True)
