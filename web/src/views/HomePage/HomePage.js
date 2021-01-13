import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';
import { Page, Header, CardHome, ListUsers } from 'components';
import gradients from 'utils/gradients';
import AttachMoneyIcon from '@material-ui/icons/AttachMoney';
import ExtensionIcon from '@material-ui/icons/Extension';
import PeopleOutlineIcon from '@material-ui/icons/PeopleOutline';
import { useSelector } from 'react-redux';
import axios from 'utils/axios';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3)
  },
  container: {  
    marginTop: theme.spacing(3)
  }
}));

const HomePage = () => {
  const classes = useStyles();

  const session = useSelector((state) => state.session);

  const [topUsers, setTopUsers] = useState([]);
  useEffect(() => {
    let mounted = true;

    const fetchUsers = () => {
      axios.get('/topUsers/', {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(response => {
        if (mounted) {
          setTopUsers(response.data.users);
        }
      });
    };

    fetchUsers();

    return () => {
      mounted = false;
    };
  }, [session.token]);

  const [numberUsers, setNumberUsers] = useState(0);
  useEffect(() => {
    let mounted = true;

    const fetchUsers = () => {
      axios.get('/users/', {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(response => {
        if (mounted) {
          setNumberUsers(response.data.users.length);
        }
      });
    };

    fetchUsers();

    return () => {
      mounted = false;
    };
  }, [session.token]);

  const [numberProducts, setNumberProducts] = useState(0);
  useEffect(() => {
    let mounted = true;

    const fetchProducts = () => {
      axios.get('/products/', {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(response => {
        if (mounted) {
          setNumberProducts(response.data.products.length);
        }
      });
    };

    fetchProducts();

    return () => {
      mounted = false;
    };
  }, [session.token]);

  const [numberSales, setNumberSales] = useState(0);
  useEffect(() => {
    let mounted = true;

    const fetchSales = () => {
      axios.get('/sales/', {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(async response => {
        if (mounted) {
          const data = response.data.sales
          const arrSum = function(arr){
            return arr.reduce(function(a,b){
              return a + b.total
            }, 0);
          }
          setNumberSales(parseFloat(arrSum(data).toFixed(2)));
        }
      });
    };

    fetchSales();

    return () => {
      mounted = false;
    };
  }, [session.token]);

  return (
    <Page
      className={classes.root}
      title="Home Page"
    >
      <Header
        titleName={'Hi ' + session.user.name}
        titleSecond="Home"
      />
      <ListUsers
        title="Top 5 Users"
        users={topUsers}
      />
      <Grid
        className={classes.container}
        container
        spacing={3}
      >
        <Grid
          item
          lg={4}
          sm={6}
          xs={12}
        >
          <CardHome
            backgroundImage={gradients.green}
            icon={<AttachMoneyIcon />}
            symbol="$"
            title="Total Sales"
            value={numberSales}            
          />
        </Grid>
        <Grid
          item
          lg={4}
          sm={6}
          xs={12}
        >
          <CardHome
            backgroundImage={gradients.blue}
            icon={<ExtensionIcon />}
            title="Total Products"
            value={numberProducts}            
          />
        </Grid>
        <Grid
          item
          lg={4}
          sm={6}
          xs={12}
        >
          <CardHome
            backgroundImage={gradients.orange}
            icon={<PeopleOutlineIcon />}
            title="Total Users"
            value={numberUsers}            
          />
        </Grid>    
      </Grid>
    </Page>
  );
};

export default HomePage;
