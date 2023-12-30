import './App.css';
import { ChakraProvider } from '@chakra-ui/react';
import Todo from './pages/Todo';

function App() {
  return (
    <ChakraProvider>
      <Todo/>
    </ChakraProvider>
  );
}

export default App;
