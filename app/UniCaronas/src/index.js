import React from 'react';
import {PersistGate} from 'redux-persist/integration/react';
import {Provider} from 'react-redux';
import App from './App';
import '~/config/reactotronConfig';
import {store, persistor} from '~/store';
import {LogBox} from 'react-native';

export default function Index() {
  //To disable yellow box set the param for true
  LogBox.ignoreAllLogs(false);

  return (
    <Provider store={store}>
      <PersistGate persistor={persistor}>
        <App />
      </PersistGate>
    </Provider>
  );
}
