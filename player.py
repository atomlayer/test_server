from flask import Blueprint
from flask import jsonify
from sql import execute, execute_array, select
from flask import request



player = Blueprint('player', __name__)


@player.route('/add_experience', methods=['POST'])
def add_experience():
    experience = int(request.form.get('experience'))
    player_id = int(request.form.get('player_id'))
    user_id = 1


    execute_array([
        ["""update ateon_player
                set experience = experience + %s
                where id = %s and user_id =%s""", (experience, player_id, user_id)],
        ["""insert into ateon_experience_events (user_id, player_id, experience_value, date)
                values (%s, %s, %s, now())""", (user_id, player_id, experience)]
    ])

    return jsonify({'message': 'Success'}), 200




@player.route('/get_experience', methods=['POST'])
def get_experience():
    player_id = int(request.form.get('player_id'))
    # user_id = 1

    res = select("""select experience from ateon_player 
              where id = %s""", (player_id,))

    return jsonify({'experience': res[0]["experience"]}), 200






@player.route('/get_player_data', methods=['GET'])
def get_player_data():
    return jsonify(message='test')