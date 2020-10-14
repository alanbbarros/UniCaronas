import React, {useEffect} from 'react';
import {Platform, StatusBar, YellowBox} from 'react-native';
import {useSelector, useDispatch} from 'react-redux';
import Navigation from '~/services/navigation';
import Routes from '~/routes';

export default function App() {
  const dispatch = useDispatch();
  const email = useSelector((state) => state.auth.email);

  console.log(email);

  return <Routes />;
}
