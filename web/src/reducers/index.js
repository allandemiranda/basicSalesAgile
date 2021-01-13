import { combineReducers } from 'redux';

import sessionReducer from './sessionReducer';
import alertReducer from './alertReducer';

const rootReducer = combineReducers({
  session: sessionReducer,
  alert: alertReducer
});

export default rootReducer;
