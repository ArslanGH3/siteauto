<template>
    <div>                
        <img 
            class="mini_profile"
            @click="getUserData"
            src="../assets/mini_profile.png"
            data-bs-toggle="modal" 
            data-bs-target="#exampleModal"
        >
        <!-- Модальное окно -->
        <div         
            class="modal fade" 
            id="exampleModal" 
            tabindex="-1" 
            aria-labelledby="exampleModalLabel" 
            aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Профиль пользователя</h5>
                <button                     
                    type="button" 
                    class="btn-close" 
                    data-bs-dismiss="modal" 
                    aria-label="Закрыть">
                </button>
            </div>
            <div class="modal-body content_user_profile">
        <!--          Пользователь авторизован-->
                <ul class="content_user_profile">
                    <li class="value_content_up">Username:&nbsp; 
                        <p class="p_content_up">{{ username }}</p></li>
                    <li class="value_content_up">Email:&nbsp; 
                        <p class="p_content_up">{{ email }}</p></li>
                </ul>
            </div>
            <div class="modal-footer">
                <button 
                    type="button" 
                    class="btn btn-secondary" 
                    data-bs-dismiss="modal">
                    Закрыть
                </button>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            email: ''
        }
    },
    methods: {
        // Функция для загрузки данных о пользователе с сервера
        async getUserData() {
            try {                
                const response = await axios.get('http://127.0.0.1:8000/api/v1/get_data_for_user_profile_ajax/')
                const data_user = response.data[0]
                this.username = data_user['username']
                this.email = data_user['email']
            } catch (error) {
                console.error(error)
            }        
        }
    }
}
</script>


<style scoped>
.mini_profile {
    cursor: pointer;
}
</style>