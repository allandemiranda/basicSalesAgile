import * as actionTypes from 'actions';

const initialState = {
  user: {},
  token: ''
};

const sessionReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SESSION_LOGIN: {
      return {
        ...state,
        token: action.token,
        user: action.user
      };
    }

    case actionTypes.SESSION_LOGOUT: {
      return {
        ...state,
        user: {},
        token: ''
      };
    }

    case actionTypes.SESSION_ERROR: {
      return {
        ...state,
        user: {},
        token: ''
      };
    }

    default: {
      return state;
    }
  }
};

export default sessionReducer;
