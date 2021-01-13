import axios from 'utils/axios';
import { newAlert } from 'actions';

export const newUser = (payload, history) => {
  return async (dispatch) => {
    const user = {      
      name: payload.values.name,
      phone: payload.values.phone,
      user_name: payload.values.user_name,
      password: payload.values.password      
    };

    const alertaError = {
      message: 'Error when registering',
      variant: 'error'
    }    

    const alertaCreate = {
      message: 'User created',
      variant: 'success'
    } 

    const response = await axios
      .post('/user', user)      
      .catch(function () {     
        console.log('AQUI') 
        return dispatch(newAlert(alertaError))        
      });
    
    if(response){
      dispatch(newAlert(alertaCreate))          
      return history.push('/auth/login')      
    }
  };
};