import {takeLatest, call, put, all, select} from 'redux-saga/effects';
import api, {CancelToken, isCancel} from '~/services/api';

let signal;

export function* signIn() {
  const {email, password} = yield select((state) => state.auth);
  signal = CancelToken.source();
}

export default all([takeLatest('@auth/SIGNIN_REQUEST', signIn)]);
