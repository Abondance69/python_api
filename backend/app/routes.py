from flask import Blueprint, jsonify
import app.services as se

api_bp = Blueprint("api", __name__)

@api_bp.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "L'API fonctionne !"}), 200

@api_bp.route("/movie/<int:movie_id>", methods=["GET"])
def get_movie_details_route(movie_id):
    data = se.get_movie_details(movie_id)
    return jsonify(data), 200

@api_bp.route("/movie/popular", methods=["GET"])
def get_popular_movies_route():
    data = se.get_popular_movies()
    return jsonify(data), 200

@api_bp.route("/movie/now_playing", methods=["GET"])
def get_now_playing_movies_route():
    data = se.get_now_playing_movies()
    return jsonify(data), 200

@api_bp.route("/movie/upcoming", methods=["GET"])
def get_upcoming_movies_route():
    data = se.get_upcoming_movies()
    return jsonify(data), 200

@api_bp.route("/movie/top_rated", methods=["GET"])
def get_top_rated_route():
    data = se.get_top_rated_movies()
    return jsonify(data), 200