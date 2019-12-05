
from flask import Blueprint, render_template
from pets_website.pets_class import Pet

main_routes = Blueprint('main', __name__, 'templates')

pet_list = Pet.populate_pet_list()


@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/pets')
def pets():
    return render_template('pets.html', pet_list=pet_list)


@main_routes.route('/pet/<pet_id>')
def pet(pet_id):
    pet = pet_list[int(pet_id)]
    return render_template('pet.html', pet=pet)

