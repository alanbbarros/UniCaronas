import produce from 'immer';

const INITIAL_STATE = {
  email: 'test1Redux',
  password: '',
  token: null,
  loading: false,
};

export default function auth(state = INITIAL_STATE, action) {
  return produce(state, (draft) => {
    switch (action.type) {
      case '@auth/SIGNIN_REQUEST': {
        if (action.payload.email && action.payload.password) {
          draft.email = action.payload.email;
          draft.password = action.payload.password;
        }
        draft.loading = true;
        break;
      }
    }
  });
}
