export function signInRequest(email = '', password = '') {
  return {
    type: '@auth/SIGNIN_REQUEST',
    payload: {email, password},
  };
}
