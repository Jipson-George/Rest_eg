from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, Resource
from models import Country
import models




parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name is required")
parser.add_argument('iso', type=str, required=True, help="ISO code is required")
parser.add_argument('isd', type=str, required=True, help="ISD code is required")
parser.add_argument('languageCode', type=str, required=True, help="Language code is required")
parser.add_argument('language', type=str, required=True, help="Language is required")
parser.add_argument('currencyCode', type=str, required=True, help="Currency code is required")
parser.add_argument('currencySymbol', type=str, required=True, help="Currency symbol is required")
parser.add_argument('minimumAge', type=int, required=False)

class CountryResource(Resource):
    def get(self):
        countries = Country.query.all()
        country_list = [{
            "id": country.id,
            "name": country.name,
            "iso": country.iso,
            "isd": country.isd,
            "languageCode": country.languageCode,
            "language": country.language,
            "currencyCode": country.currencyCode,
            "currencySymbol": country.currencySymbol,
            "minimumAge": country.minimumAge
        } for country in countries]
        return jsonify({"countries": country_list})        
    def post(self):
        args = parser.parse_args()
        country = Country(
            name=args['name'],
            iso=args['iso'],
            isd=args['isd'],
            languageCode=args['languageCode'],
            language=args['language'],
            currencyCode=args['currencyCode'],
            currencySymbol=args['currencySymbol'],
            minimumAge=args['minimumAge']
        )
        models.db.session.add(country)
        models.db.session.commit()
        return jsonify({"message": "Country added successfully", "country": {
            "id": country.id,
            "name": country.name,
            "iso": country.iso,
            "isd": country.isd,
            "languageCode": country.languageCode,
            "language": country.language,
            "currencyCode": country.currencyCode,
            "currencySymbol": country.currencySymbol,
            "minimumAge": country.minimumAge
        }})