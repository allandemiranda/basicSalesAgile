import * as actionTypes from 'actions';

const initialState = {
  user: {},
  token: '',
  erroLogin: false,
  loggedIn: false
};

const sessionReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SESSION_LOGIN: {
      return {
        ...initialState,
        loggedIn: true,
        erroLogin: false,
        token: action.token,
        user: action.user
      };
    }

    case actionTypes.SESSION_LOGOUT: {
      return {
        ...state,
        user: {},
        token: '',
        erroLogin: false,
        loggedIn: false
      };
    }

    case actionTypes.SESSION_ERROR: {
      return {
        ...state,
        user: {},
        token: '',
        erroLogin: true,
        loggedIn: false
      };
    }

    default: {
      return state;
    }
  }
};

export default sessionReducer;
