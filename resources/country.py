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
    def get(self, countryId=None):
        if countryId is not None:
            # Retrieve a single country by ID
            country = models.db.session.query(models.Country).filter_by(id=countryId).first()
            if country:
                country_data = {
                    "id": country.id,
                    "name": country.name,
                    "iso": country.iso,
                    "isd": country.isd,
                    "languageCode": country.languageCode,
                    "language": country.language,
                    "currencyCode": country.currencyCode,
                    "currencySymbol": country.currencySymbol,
                    "minimumAge": country.minimumAge
                }
                return jsonify({"country": country_data})
            else:
                return jsonify({"message": "Country not found"}), 404
        else:
            # Retrieve all countries
            countries = models.db.session.query(models.Country).all()
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
    def put(self, countryId):
        args = parser.parse_args()
        country = models.db.session.query(models.Country).filter_by(id=countryId).first()
        if not country:
            return jsonify({"message": "Country not found"}), 404

        # Update fields if they are provided in the request
        if args['name'] is not None:
            country.name = args['name']
        if args['iso'] is not None:
            country.iso = args['iso']
        if args['isd'] is not None:
            country.isd = args['isd']
        if args['languageCode'] is not None:
            country.languageCode = args['languageCode']
        if args['language'] is not None:
            country.language = args['language']
        if args['currencyCode'] is not None:
            country.currencyCode = args['currencyCode']
        if args['currencySymbol'] is not None:
            country.currencySymbol = args['currencySymbol']
        if args['minimumAge'] is not None:
            country.minimumAge = args['minimumAge']

        models.db.session.commit()

        return jsonify({"message": "Country updated successfully", "country": {
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