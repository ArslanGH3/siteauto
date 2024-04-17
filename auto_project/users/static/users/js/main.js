"use strict";


let up_username = document.getElementById('up_username');
let up_email = document.getElementById('up_email');
let mini_profile = document.getElementById('mini_profile');
let close_up_1 = document.getElementById('close_up_1');
let close_up_2 = document.getElementById('close_up_2');
let modal_block_up = document.querySelector("div.modal");


// Функция для получения данных с сервера для профиля пользователя
async function get_data_for_user_profile_ajax() {
	let url = '/api/v1/get_data_for_user_profile_ajax/';
	let response = await fetch(url);

	if (response.ok) {
		let result = await response.json();
//		Т.к. у нас список, но всегда будет только одна запись, то будем брать ее по индексу 0
		result = result[0]
        up_username.innerHTML = `${result['username']}`;
        up_email.innerHTML = `${result['email']}`;
	}
	else {
		return;
	};
};

mini_profile.addEventListener('click', get_data_for_user_profile_ajax);


function close_block_user_profile() {
    setTimeout(function(){
        up_username.innerHTML = 'null';
        up_email.innerHTML = 'null';
    }, 200);
};

modal_block_up.addEventListener('click', (event)=> {
    if (event.target == modal_block_up) {
        close_block_user_profile();
    };
});
close_up_1.addEventListener('click', close_block_user_profile);
close_up_2.addEventListener('click', close_block_user_profile);

