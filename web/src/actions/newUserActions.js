import axios from 'utils/axios';

export const REGISTRATIO_SUCCESS = 'REGISTRATIO_SUCCESS';
export const REGISTRATIO_ERROR = 'REGISTRATIO_ERROR';

export const newUser = (payload, history) => {
  return async (dispatch) => {
    const user = {      
      name: payload.values.name,
      phone: payload.values.phone,
      user_name: payload.values.user_name,
      password: payload.values.password      
    };

    await axios
      .post('/user', user)
      .then(function (response) {
        console.log(response)
        return dispatch(
          {
            type: REGISTRATIO_SUCCESS,
            nomeFuncao: 'newUser',
          },
          history.push('/auth/login')
        );
      })
      .catch(function (error) {  
        console.log(error)      
        return dispatch(
          {
            type: REGISTRATIO_ERROR,
            nomeFuncao: 'newUser',
            dados: error,
          },
          history.push('/auth/register/')
        );
        
      });
  };
};