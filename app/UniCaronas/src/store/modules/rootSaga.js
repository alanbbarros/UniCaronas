import {all} from 'redux-saga/effects';

import auth from './auth/sagas';

export default function* rootReducer() {
  return yield all([auth]);
}
