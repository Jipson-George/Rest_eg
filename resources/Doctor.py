from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from models import db, Doctor, Qualification, Specialty

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase'
db.init_app(app)

class DoctorResource(Resource):
    def __init__(self): 
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('last_name', type=str, required=True, help='Last name is required')
        self.reqparse.add_argument('first_name', type=str, required=True, help='First name is required')
        self.reqparse.add_argument('gender', type=str, required=True, help='Gender is required')
        self.reqparse.add_argument('email', type=str, required=True, help='Email is required')
        self.reqparse.add_argument('phone', type=str, required=True, help='Phone number is required')
        self.reqparse.add_argument('address_line_1', type=str)
        self.reqparse.add_argument('address_line_2', type=str)
        self.reqparse.add_argument('city', type=str, required=True, help='City is required')
        self.reqparse.add_argument('state', type=str)
        self.reqparse.add_argument('country', type=str, required=True, help='Country is required')
        self.reqparse.add_argument('postal_code', type=str)
        self.reqparse.add_argument('years_of_experience', type=int)
        self.reqparse.add_argument('description', type=str)
        self.reqparse.add_argument('photo', type=bytes)
        self.reqparse.add_argument('qualifications', type=list, location='json', required=False)
        self.reqparse.add_argument('specialties', type=list, location='json', required=False)
        super(DoctorResource, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()

        doctor = Doctor(
            last_name=args['last_name'],
            first_name=args['first_name'],
            gender=args['gender'],
            email=args['email'],
            phone=args['phone'],
            address_line_1=args.get('address_line_1'),
            address_line_2=args.get('address_line_2'),
            city=args['city'],
            state=args.get('state'),
            country=args['country'],
            postal_code=args.get('postal_code'),
            years_of_experience=args.get('years_of_experience'),
            description=args.get('description'),
            photo=args.get('photo')
        )

        qualifications = args.get('qualifications', [])
        for q in qualifications:
            qualification = Qualification(text=q)
            doctor.qualifications.append(qualification)

        specialties = args.get('specialties', [])
        for s in specialties:
            specialty = Specialty(text=s)
            doctor.specialties.append(specialty)

        db.session.add(doctor)
        db.session.commit()

        return jsonify({'message': 'Doctor registered successfully', 'doctor_id': doctor.id})

api.add_resource(DoctorResource, '/api/practitioner')

if __name__ == '__main__':
    app.run(debug=True)
